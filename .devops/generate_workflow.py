import json
from ruamel.yaml.comments import CommentedMap as ordereddict
from ruamel.yaml import YAML
from pathlib import Path

yaml_file = Path(".devops/checkout_template.yml")
yml_file = YAML()
yml_file.default_flow_style = True
template = yml_file.load(yaml_file)

with open(".devops/manifest.json") as manifest_file:
    manifest = json.load(manifest_file)

steps = []
for component, component_data in manifest.items():
    component_dict = ordereddict()
    component_dict["uses"] = "actions/checkout@v3"
    component_dict["with"] = ordereddict({
        "repository": component_data["src"],
        "path": component
    })
    steps.append(component_dict)

template["jobs"]["Checkout manifest"]["steps"] = steps

yml_file = YAML()
yaml_file = Path(".github/workflows/checkout_manifest.yml")
yml_file.dump(template, yaml_file)

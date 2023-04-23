import json

with open(".devops/manifest.json") as manifest_file:
    manifest = json.load(manifest_file)

with open(".github/workflows/checkout_manifest.yml", "w") as checkout:
    components = []
    for component in manifest.keys():
        components.append(component)

    checkout.write(str(components))

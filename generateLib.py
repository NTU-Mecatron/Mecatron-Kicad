import hashlib, json, time
import zipfile
from pathlib import Path

# Zip File
# https://realpython.com/python-zipfile/#creating-populating-and-extracting-your-own-zip-files
directory = Path(".")

include = ["footprints", "symbols", "3dmodels", "resources", "metadata.json"]
zipPath = Path("dist/mecatron-kicad-lib-1.0.0.zip")
zipPath.parent.mkdir(parents=True, exist_ok=True)   # creates dist/ if absent
installSize = 0

with zipfile.ZipFile('dist/mecatron-kicad-lib-1.0.0.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for name in include:
        entry = directory / name #join tgt

        if entry.is_file():
            zipf.write(
                entry,
                arcname=entry.relative_to(directory)
            )
            installSize += entry.stat().st_size
        else:
            for path in sorted(entry.rglob("*")):
                if path.is_file():
                    zipf.write(
                        path,
                        arcname=path.relative_to(directory)
                    )
                    installSize += path.stat().st_size
def sha256 (path): # create sha256 of file
    h = hashlib.sha256()

    #https://docs.python.org/3/library/hashlib.html#file-hashing
    with open(path, "rb") as f: 
        digest = hashlib.file_digest(f, "sha256")

    return digest.hexdigest()

zipSha = sha256(zipPath)
zipSize = zipPath.stat().st_size


# packages.json

meta = json.load(open("metadata.json"))

version = meta["versions"][0]["version"] #grab versions out 
meta["versions"][0].update({ # inject post package fields into the metadata. Defined here: https://dev-docs.kicad.org/en/addons/index.html
    #"download_url": f"https://github.com/NTU-Mecatron/Mecatron-Kicad/releases/download/v{version}/{zipPath.name}",
    "download_url": f"http://localhost:8000/dist/{zipPath.name}",
    "download_sha256": zipSha,
    "download_size": zipSize,
    "install_size": installSize,
})  

packages = {"packages": [meta]} 

pkgPath = Path("pcm/packages.json")

pkgPath.write_text(json.dumps(packages, indent=2)) #write packages.json

# repository.json

repository =  {
    "$schema": "https://go.kicad.org/pcm/schemas/v1#/definitions/Repository",
    "name": meta["name"],
    "maintainer": meta["maintainer"],
    "packages": {
        "url": "http://localhost:8000/pcm/packages.json",
        #"url": "https://raw.githubusercontent.com/NTU-Mecatron/Mecatron-Kicad/main/pcm/packages.json",
        "sha256": sha256(pkgPath),
        "update_timestamp": int(time.time()),
    },    
}

Path("pcm/repository.json").write_text(json.dumps(repository, indent=2)) #write repository.json
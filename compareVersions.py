from flask import Flask, abort, request, jsonify


app = Flask(__name__)


def compareVersions(version1, version2):
        
    versions1 = [int(v) for v in version1.split(".")]
    versions2 = [int(v) for v in version2.split(".")]
    
    for i in range(max(len(versions1),len(versions2))):
        v1 = versions1[i] if i < len(versions1) else 0
        v2 = versions2[i] if i < len(versions2) else 0
        if v1 > v2:
            return "after"
        elif v1 < v2:
            return "before"
        
    return "equal to"


@app.route("/compareVersion", methods=['GET'])
def compareVersion():
    version1 = request.args.get("version1")
    version2 = request.args.get("version2")
    
    if version1 and version2:
        return version1 + " is " + compareVersions(version1, version2) + " " + version2
    else:
        abort(400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, threaded=True)
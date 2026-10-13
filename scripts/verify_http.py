"""Real loopback HTTP supplement, independent of Docker and fixed test counts."""
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import threading
from urllib.error import HTTPError
from urllib.request import urlopen
from werkzeug.serving import make_server

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app import create_app


if __name__ == '__main__':
    output = ROOT/'evidence/local-http-results.json'
    if output.exists():
        sys.exit('Evidence exists; do not overwrite.')
    app = create_app()
    server = make_server('127.0.0.1', 0, app)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    results = []
    try:
        expected = [('/api/hello',200,{'message':'Hello','version':'v2','place':app.config['APP_PLACE']}),
                    ('/api/health',200,{'status':'ok','service':'t05-stateless-handover'}),
                    ('/api/info',200,{'project':'T05 Stateless Handover Lab','runtime':'Flask','handover':True}),
                    ('/api/not-found',404,{'error':'not_found'})]
        for path,status,body in expected:
            try:
                response = urlopen(f'http://127.0.0.1:{server.server_port}{path}',timeout=5)
            except HTTPError as error:
                response = error
            with response:
                actual = json.load(response)
                results.append({'path':path,'http_status':response.code,'body':actual,
                                'passed':response.code == status and actual == body})
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()
    data = {'executed_at':datetime.now(timezone.utc).isoformat(),'kind':'local_http_not_docker',
            'host':'127.0.0.1','port':server.server_port,'results':results}
    output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(data,indent=2))
    sys.exit(0 if all(r['passed'] for r in results) else 1)

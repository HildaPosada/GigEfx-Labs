"""Collect a timestamped public-feed snapshot and preserve versioned history."""
import urllib.request,json,datetime,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def collect():
 url='https://littlebirdelectronics.com.au/public-api/v1/products?per_page=25&q=raspberry'
 with urllib.request.urlopen(url,timeout=30) as response:raw=response.read()
 feed=json.loads(raw);rows=[];excluded=0
 for p in feed['products']:
  if not isinstance(p.get('price'),(int,float)) or p['price']<=0 or p.get('price_currency')!='AUD':excluded+=1;continue
  rows.append({k:p.get(k) for k in ['handle','title','price','price_currency','in_stock','sku']})
 path=ROOT/'web/history.json';history=json.loads(path.read_text()) if path.exists() else {'source':url,'currency':'AUD','observations':[]}
 snapshot={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(raw).hexdigest(),'excluded_rows':excluded,'products':rows};history['observations'].append(snapshot)
 path.write_text(json.dumps(history,indent=2)+'\n');print('Persisted',len(rows),'products;',excluded,'invalid-priced rows excluded')
if __name__=='__main__':collect()

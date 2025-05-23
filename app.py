from matplotlib.figure import Figure
from io import BytesIO
from flask import Flask
import base64
import psutil

app = Flask(__name__)

@app.route('/')


def mainplot():
   partitions = psutil.disk_partitions()
   partlen = len(partitions)
   d={}
   fig = Figure()
   #ax = fig.subplots(partlen)
   fig.suptitle('Disk Utilization', fontsize=16)
   for index, p in enumerate(partitions, start=1):
      #print(index,p.mountpoint, psutil.disk_usage(p.mountpoint).percent)
      #print(p)
      diskusage=psutil.disk_usage(p.mountpoint)
      labels = 'Used', 'Free'
      d[f"sizes{index}"] = [diskusage.used,diskusage.free]
      #labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
      #sizes = [15, 30, 45, 10]
      #fig = Figure()
      #d[f"fig{index}"].suptitle(p.mountpoint)
      #subplotparam=f"12{index}"
      #print(subplotparam)
      ax = fig.add_subplot(partlen,partlen,index)
      ax.set_title(f"{p.mountpoint}")
      ax.pie(d[f"sizes{index}"],labels=labels)
   buf = BytesIO()
   fig.savefig(buf, format="png")
   data = base64.b64encode(buf.getbuffer()).decode("ascii")
   return f"<img src='data:image/png;base64,{data}'/>"

if __name__ == '__main__':
    app.run(debug=True)

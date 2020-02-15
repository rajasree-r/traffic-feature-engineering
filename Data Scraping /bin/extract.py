{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"extract.py","provenance":[]},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"oBAXdwxdvfVd","colab_type":"code","outputId":"160faf54-3529-44d9-a78a-e0cd60686124","executionInfo":{"status":"ok","timestamp":1579806124991,"user_tz":480,"elapsed":277,"user":{"displayName":"Naga Sindhu Korlapati","photoUrl":"","userId":"02414744571167674372"}},"colab":{"base_uri":"https://localhost:8080/","height":34}},"source":["import importlib.util\n","import sys\n","from google.colab import drive\n","\n","drive.mount('/content/drive')"],"execution_count":0,"outputs":[{"output_type":"stream","text":["Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"],"name":"stdout"}]},{"cell_type":"code","metadata":{"id":"lOlchN-IvlJv","colab_type":"code","outputId":"574f93b2-8ab0-4d33-cb17-3051324c7ab1","executionInfo":{"status":"error","timestamp":1579807510013,"user_tz":480,"elapsed":819,"user":{"displayName":"Naga Sindhu Korlapati","photoUrl":"","userId":"02414744571167674372"}},"colab":{"base_uri":"https://localhost:8080/","height":405}},"source":["import sys\n","sys.path.append(\"pems_extract\")\n","print(sys.path)\n","from pems_extractor import PemsExtractor\n","from utils import locate_config\n","\n","\n","if __name__ == \"__main__\":\n","\n","    config_path = locate_config(sys.argv)\n","\n","    pems = PemsExtractor(config_path)\n","    links = pems.extract_links()\n","    print(\"extracted Links, found: \", len(links))\n","\n","    pems.get_files(links)"],"execution_count":0,"outputs":[{"output_type":"stream","text":["['', '/env/python', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages', '/usr/local/lib/python3.6/dist-packages/IPython/extensions', '/root/.ipython', './src', './src/pems_extract/', './src/pems_extract/', './src/', './src/', '/content/drive/Shared drives/DATA298B/Data Scraping/src/', '/content/drive/Shared drives/DATA298B/Data Scraping/src/', '/content/drive/Shared drives/DATA298B/Data Scraping/src/', '/content/drive/Shared drives/DATA298B/Data Scraping/src/pems_extract', '/content/drive/Shared drives/DATA298B/', '/content/drive/Shared drives/DATA298B/Data Scraping/src/pems_extract/', '/content/drive/Shared drives/DATA298B/Data Scraping/src/pems_extract/', 'pems_extract']\n"],"name":"stdout"},{"output_type":"error","ename":"ModuleNotFoundError","evalue":"ignored","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)","\u001b[0;32m<ipython-input-16-570c34da5004>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"pems_extract\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mpems_extractor\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mPemsExtractor\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mutils\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mlocate_config\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pems_extractor'","","\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"]}]},{"cell_type":"code","metadata":{"id":"M5aCG0ICvwqV","colab_type":"code","colab":{}},"source":[""],"execution_count":0,"outputs":[]}]}
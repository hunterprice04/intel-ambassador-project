# intel-ambassador-project

# setting up python-embree in linux
```bash
$ cd python-embree
$ python setup.py build_ext -I/c/Program\ Files/Intel/Embree3/include -L /c/Program\ Files/Intel/Embree3/lib
$ python setup.py install
```
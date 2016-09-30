class GetSet(object):
    instance_count = 0

    __mangled_name = 'no privacy'   # can be accesed only by a special syntax

    def __init__(self, value):
        self._attrval = value   # inward-facing name that we use internally
        GetSet.instance_count += 1

    @property
    def var(self):  # outward-facing name that we want users to use
        print('getting the "var" attribute')
        return self._attrval

    @var.setter
    def var(self, value):
        print('setting the "var" attribute')
        self._attrval = value

    @var.deleter
    def var(self):
        print('deleting the "var" attribute')
        self._attrval = None


me = GetSet(5)

me.var = 1000
print me.var
del me.var
print me.var
print me._attrval
print me.instance_count
print me._GetSet__mangled_name
print GetSet._GetSet__mangled_name


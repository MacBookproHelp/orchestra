# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

class yc_flow_wired_to_orc__ControllerMac_Switches_flows_flow(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module wired_to_orc - based on the path /ControllerMac/Switches/flows/flow. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ip_src','__ip_dst','__port','__throughput',)

  _yang_name = 'flow'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ip_dst = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip_dst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='ipv4-address', is_config=True)
    self.__throughput = YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={u'range': [u'1..3.14', u'10', u'20..max']}), is_leaf=True, yang_name="throughput", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='throughput', is_config=True)
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={u'range': [u'0..65535']}), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='port-number', is_config=True)
    self.__ip_src = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip_src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='ipv4-address', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'ControllerMac', u'Switches', u'flows', u'flow']

  def _get_ip_src(self):
    """
    Getter method for ip_src, mapped from YANG variable /ControllerMac/Switches/flows/flow/ip_src (ipv4-address)
    """
    return self.__ip_src
      
  def _set_ip_src(self, v, load=False):
    """
    Setter method for ip_src, mapped from YANG variable /ControllerMac/Switches/flows/flow/ip_src (ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_src is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_src() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip_src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_src must be of a type compatible with ipv4-address""",
          'defined-type': "wired_to_orc:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip_src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='ipv4-address', is_config=True)""",
        })

    self.__ip_src = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_src(self):
    self.__ip_src = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip_src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='ipv4-address', is_config=True)


  def _get_ip_dst(self):
    """
    Getter method for ip_dst, mapped from YANG variable /ControllerMac/Switches/flows/flow/ip_dst (ipv4-address)
    """
    return self.__ip_dst
      
  def _set_ip_dst(self, v, load=False):
    """
    Setter method for ip_dst, mapped from YANG variable /ControllerMac/Switches/flows/flow/ip_dst (ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_dst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_dst() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip_dst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_dst must be of a type compatible with ipv4-address""",
          'defined-type': "wired_to_orc:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip_dst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='ipv4-address', is_config=True)""",
        })

    self.__ip_dst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_dst(self):
    self.__ip_dst = YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_dict={u'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ip_dst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='ipv4-address', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /ControllerMac/Switches/flows/flow/port (port-number)
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /ControllerMac/Switches/flows/flow/port (port-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={u'range': [u'0..65535']}), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='port-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with port-number""",
          'defined-type': "wired_to_orc:port-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={u'range': [u'0..65535']}), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='port-number', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={u'range': [u'0..65535']}), is_leaf=True, yang_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='port-number', is_config=True)


  def _get_throughput(self):
    """
    Getter method for throughput, mapped from YANG variable /ControllerMac/Switches/flows/flow/throughput (throughput)
    """
    return self.__throughput
      
  def _set_throughput(self, v, load=False):
    """
    Setter method for throughput, mapped from YANG variable /ControllerMac/Switches/flows/flow/throughput (throughput)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_throughput is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_throughput() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=Decimal, restriction_dict={u'range': [u'1..3.14', u'10', u'20..max']}), is_leaf=True, yang_name="throughput", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='throughput', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """throughput must be of a type compatible with throughput""",
          'defined-type': "wired_to_orc:throughput",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={u'range': [u'1..3.14', u'10', u'20..max']}), is_leaf=True, yang_name="throughput", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='throughput', is_config=True)""",
        })

    self.__throughput = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_throughput(self):
    self.__throughput = YANGDynClass(base=RestrictedClassType(base_type=Decimal, restriction_dict={u'range': [u'1..3.14', u'10', u'20..max']}), is_leaf=True, yang_name="throughput", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='throughput', is_config=True)

  ip_src = __builtin__.property(_get_ip_src, _set_ip_src)
  ip_dst = __builtin__.property(_get_ip_dst, _set_ip_dst)
  port = __builtin__.property(_get_port, _set_port)
  throughput = __builtin__.property(_get_throughput, _set_throughput)


  _pyangbind_elements = OrderedDict([('ip_src', ip_src), ('ip_dst', ip_dst), ('port', port), ('throughput', throughput), ])


class yc_flows_wired_to_orc__ControllerMac_Switches_flows(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module wired_to_orc - based on the path /ControllerMac/Switches/flows. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__flow',)

  _yang_name = 'flows'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__flow = YANGDynClass(base=YANGListType("port",yc_flow_wired_to_orc__ControllerMac_Switches_flows_flow, yang_name="flow", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port', extensions=None), is_container='list', yang_name="flow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='list', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'ControllerMac', u'Switches', u'flows']

  def _get_flow(self):
    """
    Getter method for flow, mapped from YANG variable /ControllerMac/Switches/flows/flow (list)
    """
    return self.__flow
      
  def _set_flow(self, v, load=False):
    """
    Setter method for flow, mapped from YANG variable /ControllerMac/Switches/flows/flow (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flow is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flow() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("port",yc_flow_wired_to_orc__ControllerMac_Switches_flows_flow, yang_name="flow", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port', extensions=None), is_container='list', yang_name="flow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flow must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("port",yc_flow_wired_to_orc__ControllerMac_Switches_flows_flow, yang_name="flow", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port', extensions=None), is_container='list', yang_name="flow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='list', is_config=True)""",
        })

    self.__flow = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flow(self):
    self.__flow = YANGDynClass(base=YANGListType("port",yc_flow_wired_to_orc__ControllerMac_Switches_flows_flow, yang_name="flow", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port', extensions=None), is_container='list', yang_name="flow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='list', is_config=True)

  flow = __builtin__.property(_get_flow, _set_flow)


  _pyangbind_elements = OrderedDict([('flow', flow), ])


class yc_Switches_wired_to_orc__ControllerMac_Switches(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module wired_to_orc - based on the path /ControllerMac/Switches. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__flows',)

  _yang_name = 'Switches'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__flows = YANGDynClass(base=yc_flows_wired_to_orc__ControllerMac_Switches_flows, is_container='container', yang_name="flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'ControllerMac', u'Switches']

  def _get_flows(self):
    """
    Getter method for flows, mapped from YANG variable /ControllerMac/Switches/flows (container)
    """
    return self.__flows
      
  def _set_flows(self, v, load=False):
    """
    Setter method for flows, mapped from YANG variable /ControllerMac/Switches/flows (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flows is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flows() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_flows_wired_to_orc__ControllerMac_Switches_flows, is_container='container', yang_name="flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flows must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_flows_wired_to_orc__ControllerMac_Switches_flows, is_container='container', yang_name="flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)""",
        })

    self.__flows = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flows(self):
    self.__flows = YANGDynClass(base=yc_flows_wired_to_orc__ControllerMac_Switches_flows, is_container='container', yang_name="flows", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)

  flows = __builtin__.property(_get_flows, _set_flows)


  _pyangbind_elements = OrderedDict([('flows', flows), ])


class yc_ControllerMac_wired_to_orc__ControllerMac(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module wired_to_orc - based on the path /ControllerMac. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__Switches',)

  _yang_name = 'ControllerMac'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__Switches = YANGDynClass(base=yc_Switches_wired_to_orc__ControllerMac_Switches, is_container='container', yang_name="Switches", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'ControllerMac']

  def _get_Switches(self):
    """
    Getter method for Switches, mapped from YANG variable /ControllerMac/Switches (container)
    """
    return self.__Switches
      
  def _set_Switches(self, v, load=False):
    """
    Setter method for Switches, mapped from YANG variable /ControllerMac/Switches (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_Switches is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_Switches() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_Switches_wired_to_orc__ControllerMac_Switches, is_container='container', yang_name="Switches", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """Switches must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_Switches_wired_to_orc__ControllerMac_Switches, is_container='container', yang_name="Switches", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)""",
        })

    self.__Switches = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_Switches(self):
    self.__Switches = YANGDynClass(base=yc_Switches_wired_to_orc__ControllerMac_Switches, is_container='container', yang_name="Switches", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)

  Switches = __builtin__.property(_get_Switches, _set_Switches)


  _pyangbind_elements = OrderedDict([('Switches', Switches), ])


class wired_to_orc(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module wired_to_orc - based on the path /wired_to_orc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_path_helper', '_extmethods', '__ControllerMac',)

  _yang_name = 'wired_to_orc'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__ControllerMac = YANGDynClass(base=yc_ControllerMac_wired_to_orc__ControllerMac, is_container='container', yang_name="ControllerMac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_ControllerMac(self):
    """
    Getter method for ControllerMac, mapped from YANG variable /ControllerMac (container)
    """
    return self.__ControllerMac
      
  def _set_ControllerMac(self, v, load=False):
    """
    Setter method for ControllerMac, mapped from YANG variable /ControllerMac (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ControllerMac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ControllerMac() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_ControllerMac_wired_to_orc__ControllerMac, is_container='container', yang_name="ControllerMac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ControllerMac must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_ControllerMac_wired_to_orc__ControllerMac, is_container='container', yang_name="ControllerMac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)""",
        })

    self.__ControllerMac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ControllerMac(self):
    self.__ControllerMac = YANGDynClass(base=yc_ControllerMac_wired_to_orc__ControllerMac, is_container='container', yang_name="ControllerMac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='https://wired.com/wired_to_orc', defining_module='wired_to_orc', yang_type='container', is_config=True)

  ControllerMac = __builtin__.property(_get_ControllerMac, _set_ControllerMac)


  _pyangbind_elements = OrderedDict([('ControllerMac', ControllerMac), ])



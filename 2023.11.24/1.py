class ClassBuilder: 
    def __init__(self, class_name): 
        self.class_name = class_name 
        self.cls_fields = [] 
        self.inst_attrs = [] 
         
    def add_cls_field(self, name, value): 
        self.cls_fields.append((name, value)) 
        return self 
     
    def add_inst_attr(self, name, value): 
        self.inst_attrs.append((name, value)) 
        return self 
     
    def __str__(self): 
        cls_fields_str = "\n".join(f"       {name}= {repr(value)}" for name, value in self.cls_fields) 
        inst_attrs_str = "\n".join(f"       self.{name} = {repr(value)}" for name, value in self.inst_attrs) 
         
        if not cls_fields_str: 
            cls_fields_str = '      pass' 
             
        return f"class {self.class_name}:\n{cls_fields_str}\n\n    def __init__(self):\n{inst_attrs_str}"
    
    
# cb = ClassBuilder('Person').add_cls_field('field1', 'value1').add_inst_attr('name', '').add_inst_attr('age', 0)
# print(cb)

# cb = ClassBuilder('Test').add_cls_field('__protected', []).add_inst_attr('foo', 'bar')
# print(cb)

# cb = ClassBuilder('Foo')
# print(cb)            
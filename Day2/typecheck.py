multi_type_list=[10,3.14,"program",28];


for val in multi_type_list:	 
      integer=isinstance(val,int)
      floatvalue=isinstance(val,float)
      string=isinstance(val, str )
      if integer:
        print(val+1);
      if floatvalue:
        print(val+1);
      if string:      
        print(val.upper());
	

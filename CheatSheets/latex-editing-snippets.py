import numpy as np

def removeabstracts(bibfile, printabstract=False):
  """This function rewrites bibfile entries to remove the abstract line for a more streamlined set of references. It can be altered for other parts of an entry e.g. to remove dates."""
  refs = open(bibfile,'r')
  lines = refs.readlines()
  # print(lines)

  new_lines = []
  for line in lines:
    if "abstract" not in line.strip():
        new_lines.append(line)
    else:
      if printabstract==True:  
        print(line)

  file = open(bibfile, "w")
  file.writelines(new_lines)
  file.close()

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  fp = open(filename,"a")
  fp.write(comments)
  fp.close()
  return(os.path.getsize(filename))

print(create_python_script("program.py"))

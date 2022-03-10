
# def find():
#     a = "ab"
#     e = "aa"
#     a = list(a)
#     e = list(e)

#     if len(a)>len(e):
#         for i in a:
#             if i not in e:
#                 return i
#             for l in e:
#                 if l == i:
#                     return i
#     else:
#         for i in e:
#             if i not in a:
#                 return i
#             for l in e:
#                 if l == i:
#                     return i
            
        


# print(find())


import subprocess


print(subprocess.getoutput("djrun"))
subprocess.call("python management runserver")


# funcion even
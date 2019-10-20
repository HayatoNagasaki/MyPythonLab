import js2py



js = """
function escramble_758(){
var a,b,c
a=1
b=2
c=3
return (a+b+c+d)
}
escramble_758()
""".replace("d", "100")

result = js2py.eval_js(js)

print(result)

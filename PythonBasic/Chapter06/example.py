#import myCalcPackage
#from myCalcPackage import calcModule
import sys
sys.path.append("D:/Pywork/DataScience")
from myCalcPackage import calcModule
x = 10
y = 5

print(f'x = {x}; y= {y} 일 때')
calcModule.Add(x, y)
calcModule.Sub(x, y)
calcModule.Mul(x, y)
calcModule.Div(x, y)


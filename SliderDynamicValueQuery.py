import maya.cmds as cmds


def fun(arg):
	print arg


def createWin():	
	try:
		cmds.deleteUI("myWindow")
	except:
		print 'no window to delete currently'
	
	cmds.window("myWindow")
	cmds.columnLayout( adjustableColumn=True )
	queriedValueInplace = cmds.intSliderGrp(label='Slider to query value in place', minValue=4, maxValue=20, value=12, field=True, dc = lambda *args: fun(cmds.intSliderGrp(queriedValueInplace, query=True, value=True)) )
	
	cmds.showWindow()

createWin()


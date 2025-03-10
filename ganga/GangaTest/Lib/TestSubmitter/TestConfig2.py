# Definition of config - as it comes in the plugin code

import GangaCore.Utility.Config
cc = GangaCore.Utility.Config.makeConfig('TestConfig2', 'more testing stuff')

cc.addOption('str1', '', 'doc')
cc.addOption('str2', '', 'doc')
cc.addOption('str3', '', 'doc')
cc.addOption('str4', '', 'doc')
cc.addOption('str5', '', 'doc')
cc.addOption('str6', '', 'doc')
cc.addOption('str7', '', 'doc')
cc.addOption('str8', '', 'doc')

cc.addOption('int1', 0, 'doc')
cc.addOption('int2', 0, 'doc')
cc.addOption('int3', 0, 'doc')
cc.addOption('int4', 0, 'doc')
cc.addOption('int5', 0, 'doc')
cc.addOption('int6', 0, 'doc')
cc.addOption('int7', 0, 'doc')
cc.addOption('int8', 0, 'doc')

cc.addOption('none1', None, 'doc')
cc.addOption('none2', None, 'doc')
cc.addOption('none3', None, 'doc')
cc.addOption('none4', None, 'doc')
cc.addOption('none5', None, 'doc')
cc.addOption('none6', None, 'doc')
cc.addOption('none7', None, 'doc')
cc.addOption('none8', None, 'doc')

cc.addOption('list1', [], 'doc')
cc.addOption('list2', [], 'doc')
cc.addOption('list3', [], 'doc')
cc.addOption('list4', [], 'doc')
cc.addOption('list5', [], 'doc')
cc.addOption('list6', [], 'doc')
cc.addOption('list7', [], 'doc')
cc.addOption('list8', [], 'doc')

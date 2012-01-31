import gtk

import player.ListPlayer
import music_lists
import music_collections

import inspect

import os
import sys
import constants

import threading

class PympDaemon():
    def __init__(self):
        print "Starting the daemon"
        
        #Initialize the required objects
        list_manager = music_lists.ListManager()
        list_player = player.ListPlayer.ListPlayer()
        collections_manager = music_collections.CollectionManager()
        
        #Load/enable the API
        #daemon_api.API(list_manager, list_player, collections_manager)
        
        #Loading plugins. Note plugins are located in the plugins-dir, which 
        #  can be found two levels higher than this file. TODO: Renice this,
        #  getting this dir somewhere else instead of finding it out ourselves.
        pluginpath = os.path.dirname(os.path.dirname(unicode(inspect.getfile( inspect.currentframe() ) ) )) + "/plugins"
        plugin_manager = PluginManager( pluginpath , list_player)
        plugin_manager.loadAll(listPlayer=list_player, listManager=list_manager, collectionManager=collections_manager)
                
        #start all plugins
        for plugin in plugin_manager.getPlugins():
            print "Starting plugin: "+unicode(plugin)
            plugin_manager.startPlugin(plugin)
        
        
        collections_manager.load_collections()
        
        gtk.main()







class PluginManager:
    
    def __init__(self, folder, listPlayer):
        self._folder = folder
        self._plugins =  {}
        self.listPlayer = listPlayer

    
    def loadAll(self, **kwargs):
        for dirfile in os.listdir(self._folder):
            fulldir = self._folder+"/"+dirfile
            if os.path.isdir(fulldir):
                self.loadPlugin(dirfile, **kwargs)
    
    
    def loadPlugin(self, name, **kwargs):
        # Try to import the module
        modulename = "plugins."+name
        try:
            __import__(modulename)
        except Exception as e:
            print "Plugin: Import "+name+ " failed: "+unicode(e)
            return
        
        plugin = sys.modules[modulename]
        
        try:
            plugin.info["class"]
        except:
            print "Plugin: Import "+name+ " failed: no info['class'] available."
        
        if hasattr(plugin, plugin.info["class"]):
            try:
                self._plugins[name] = getattr(plugin, plugin.info["class"])(**kwargs)
                print "Plugin: Loaded %s" % name
            except Exception as e:
                print "Plugin: Loading failed for "+name+"! ("+unicode(e)+")"
    
    def getPlugins(self):
        return self._plugins.keys()
     

    def startPlugin(self, name):
        plugin = self._plugins[name]
        plugin.start()
        
        
    def stopPlugin(self, name):
        plugin = self._plugins[name]
        plugin.stop()
        

PympDaemon()

"""
Utilities for Project DJ
"""
import os, shutil


def recursive_file_gen(src_dir, dest_dir, project_name):
    """
    Recursively generate files from an src_dir to a dest_dir
    """
    for root, dirs, files in os.walk(src_dir):
        
        for directory in dirs:
            if directory.startswith('.'):
                dirs.remove(directory)
            
        for directory in dirs:            
            placement = os.path.join("%s" % root, "%s" % directory)
            placement = placement.replace(src_dir, dest_dir)
            if not os.path.isdir(placement):
                os.mkdir(placement)
                
        for the_file in files:
            if not the_file.endswith(".pyc") and not the_file.startswith("."):
                if root.find('/.') == -1 and root.find('\\.') == -1:
                    orig = os.path.join(root, the_file)
                    placement = orig.replace(src_dir, dest_dir)
                    shutil.copy(orig, placement)
                    
                    if str(placement).endswith("py"):
                        file_to_mod = open(placement)
                        file_str = file_to_mod.read()
                        file_to_mod.close()
                        file_str = str(file_str)
                        
                        mod_str = file_str.replace("PROJECTDJPROJECT", project_name)
                        file_to_mod = open(placement, "w")
                        file_to_mod.write(mod_str)
                        file_to_mod.close()
                        
                        
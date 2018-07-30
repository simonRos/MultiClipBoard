#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcb_shelf = shelve.open('mcb')

if len(sys.argv) == 3:
    #save with name
    if sys.argv[1].lower() == '-s':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    #delete by name
    elif sys.argv[1].lower() == '--delete':
        #if no entry by this name exists, don't bother.
        if sys.argv[2] in mcb_shelf:
            #deletion is handled by making the element blank
            mcb_shelf.pop(sys.argv[2])
    #examine specific clipboard
    elif sys.argv[1].lower() == '-e':
        print(sys.argv[2]+":\n"+mcb_shelf[sys.argv[2]])
elif len(sys.argv) == 2:
    #help
    if sys.argv[1].lower() == '-h':
        print("-d arg    delete a clipboard")
        print("-e arg    examine a clipboard")
        print("-h        command help")
        print("-l        list all clipboards")
        print("-s        saves a clipboard")
        print("-s arg    saves a clipboard with a name")
        print("-w        wipes all clipboards")
        
    #save generic
    elif sys.argv[1].lower() == '-s':
        #generic key construction
        temp_key = len(list(mcb_shelf))
        while str(temp_key) in mcb_shelf.keys():
            temp_key += 1
        mcb_shelf[str(temp_key)] = pyperclip.paste()
    #list all on console
    elif sys.argv[1].lower() == '-l':
        for k in mcb_shelf.keys():
            #cliboard contents
            valu = str(mcb_shelf[k])
            #shrink for display readability
            out = k + ": " + valu[0:64]
            #replace out newlines and tabs for display readability
            out = out.replace('\r', '').replace('\n', '').replace('\t','')
            #space saver to indicate more content exists
            if len(valu) > 64:
                out = out[0:61] + '...'
            print(out)        
    #wipe all
    elif sys.argv[1].lower() == '--wipe':
        print(len(list(mcb_shelf)), "cliboard(s) exist. Wipe them?")
        if input("[y/n]\n").lower() == 'y':
            mcb_shelf.clear()
    #retrieve
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    
mcb_shelf.close

# print region data

values = [(0,8),
          (9,16),
          (17,25),
          (26,33),
          (34,42),
          (43,50),
          (51,59),
          (60,67),
          (68,76),
          (77,84),
          (85,93),
          (94,101),
          (102,110),
          (111,118),
          (119,127),
          (0,0)]         # out of range

for i in range(8):
    pair_old, pair_new = values[2*i-1], values[2*i+1]
    print("<group> // wave "+str(i)+" trigger")
    print("  trigger=first")
    print("  group="+str(i))
    print("  off_by="+str(i))
    print()
    print("  <region>")
    print("    xfin_locc2="+str(pair_old[0]))
    print("    xfin_hicc2="+str(pair_old[1]))
    print("    xfout_locc2="+str(pair_new[0]))
    print("    xfout_hicc2="+str(pair_new[1]))
    print()
    print("    sample=$WAVE"+str(i))
    print()
    print("<group> // wave "+str(i)+" legato")
    print("  trigger=legato")
    print("  group="+str(i))
    print("  off_by="+str(i))
    print()
    print("  <region>")
    print("    xfin_locc2="+str(pair_old[0]))
    print("    xfin_hicc2="+str(pair_old[1]))
    print("    xfout_locc2="+str(pair_new[0]))
    print("    xfout_hicc2="+str(pair_new[1]))
    print()
    print("    sample=$WAVE"+str(i))
    print()

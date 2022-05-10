start = str(input("Would you like to begin now? [yes/no]"))
while start == 'yes' or 'yess':
   numberofattempts=int(8)
   a = float(input("What is the value of A?"))
   b = float(input("What is the value of B?"))
   c = float(input("What is the value of C?"))
   volume=float(a*b*c)
   surfacearea=float((a*c*2+c*b*2+a*b*2)+(c*2*2+a*2*4+b*2))
   if start == 'yes':
     lowestsurfacearea=surfacearea
   start='no'
   ratio=float(surfacearea/volume)
   print ('Value of A:',a)
   print ('Value of B:',b)
   print ('Value of C:',c)
   print ('Volume:',volume)
   print ('Surface Area:',surfacearea)
   print ('Surface Area to Volume Ratio: ',ratio,':1')
   a = float(input("What is the value of A?"))
   b = float(input("What is the value of B?"))
   c = float(input("What is the value of C?"))
   volume=float(a*b*c)
   surfacearea=float((a*c*2+c*b*2+a*b*2)+(c*2*2+a*2*4+b*2))
   ratio=float(surfacearea/volume)
   print ('Value of A:',a)
   print ('Value of B:',b)
   print ('Value of C:',c)
   print ('Volume:',volume)
   print ('Surface Area:',surfacearea)
   print ('Surface Area to Volume Ratio: ',ratio,':1')
   if surfacearea < lowestsurfacearea:
      lowestsurfacearea=surfacearea
      print ('Combination of factors of 1500 with lowest surface area from given input found. Refer to above for factors.')
   for x in range(numberofattempts):
      a = float(input("What is the value of A?"))
      b = float(input("What is the value of B?"))
      c = float(input("What is the value of C?"))
      volume=float(a*b*c)
      surfacearea=float((a*c*2+c*b*2+a*b*2)+(c*2*2+a*2*4+b*2))
      ratio=float(surfacearea/volume)
      print ('Value of A:',a)
      print ('Value of B:',b)
      print ('Value of C:',c)
      print ('Volume:',volume)
      print ('Surface Area:',surfacearea)
      print ('Surface Area to Volume Ratio: ',ratio,':1')
      
      if surfacearea < lowestsurfacearea:
         lowestsurfacearea=surfacearea
         print ('Combination of factors of 1500 with lowest surface area from given input found. Refer to above for factors.')
   retry = str(input("Would you like to continue? [yes/no]"))
   if retry == 'yes':
      start='yess'
   else:
      exit()

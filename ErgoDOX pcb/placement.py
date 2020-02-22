import pcbnew

board = pcbnew.GetBoard()

#ds=pcbnew.DRAWSEGMENT(pcb)
#self._board.Add(ds)
#ds.SetShape(pcbnew.S_SEGMENT)
#ds.SetStart(pcbnew.wxPoint(1, 1))
#ds.SetEnd(pcbnew.wxPoint(10, 10))
#ds.SetLayer(pcb._LayerNumByName["B.SilkS"])
#ds.SetWidth(int(0.15*pcbnew.IU_PER_MM))

 
#em = pcbnew.EDGE_MODULE(pcb)

print("Hello")
pos = board.GetPosition()
print("Board position: " + pos)


for module in board.GetModules():
  reference = module.GetReference()
  if (reference.startswith('SW')):
    print(module.GetReference()),
    print(module.GetPosition())


#pcbnew.Refresh()
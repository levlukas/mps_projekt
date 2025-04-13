[Noise Spectral Density - (V/Hz½ or A/Hz½)]
{
   Npanes: 2
   {
      traces: 1 {589826,0,"v(onoise)*v(onoise)/100"}
      X: ('K',0,1,0,150000)
      Y[0]: ('f',7,2.289e-19,7e-22,2.359e-19)
      Y[1]: ('n',1,1e+308,1e-10,-1e+308)
      Units: "V²/Hz" ('f',0,0,1,2.289e-19,7e-22,2.359e-19)
      Log: 1 0 0
      GridStyle: 1
   },
   {
      traces: 1 {524291,0,"v(onoise)/100"}
      X: ('K',0,1,0,150000)
      Y[0]: ('p',2,4.781e-11,7e-14,4.858e-11)
      Y[1]: ('n',1,1e+308,1e-10,-1e+308)
      Units: "V/Hz½" ('p',0,0,2,4.781e-11,7e-14,4.858e-11)
      Log: 1 0 0
      GridStyle: 1
   }
}
[Operating Point]
{
   Npanes: 1
   {
      traces: 2 {303038467,0,"I(Vcc)"} {524290,1,"(V(in)-V(col))*I(Rload)"}
      X: ('K',0,1,10000,150000)
      Y[0]: ('n',1,6e-10,2e-10,2.8e-09)
      Y[1]: ('n',1,-1e-09,2e-10,1.2e-09)
      Amps: ('n',0,0,1,6e-10,2e-10,2.8e-09)
      Units: "W" ('n',0,0,1,-1e-09,2e-10,1.2e-09)
      Log: 0 0 0
      GridStyle: 1
   }
}

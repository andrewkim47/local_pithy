strings = [
'C LFP 1500 CT Air2 1C CCCV 2.0cyc Coldtemp 200cyc 20180813 220023-7-2-160 ',
'C LFP 1500 CT Air1 1C CCCV 2.0cyc Coldtemp 200cyc 20180813 220023-7-1-160 ',
'C ICR 2600 CT Air2 1C CCCV 2.0cyc coldtemp 200cyc 20180813 220023-6-2-160 ',
'C LFP 1500 CT Oil1 1C CCCV 2.0cyc Coldtemp 200cyc 20180813 220023-7-3-160 ',
'C LFP 1500 CT Oil2 1C CCCV 2.0cyc Coldtemp 200cyc 20180813 220023-7-4-160 ',
'C LFP 1500 CT Water2 1C CCCV 2.0cyc Coldtemp 200cyc 20180813 220023-7-6-160 ',
'C ICR 2600 CT Air1 1C CCCV 2.0cyc coldtemp 200cyc 20180813 220023-6-1-160 ',
'C ICR 2600 CT Oil2 1C CCCV 2.0cyc coldtemp 200cyc 20180813 220023-6-4-160 ',
'C LFP 1500 CT Water1 1C CCCV 2.0cyc Coldtemp 200cyc 20180813 220023-7-5-160 ',
'C ICR 2600 CT Water2 1C CCCV 2.0cyc coldtemp 200cyc 20180813 220023-6-6-160 ',
'C ICR 2600 CT Oil1 1C CCCV 2.0cyc coldtemp 200cyc 20180813 220023-6-3-160 ',
'C ICR 2600 CT Water1 1C CCCV 2.0cyc coldtemp 200cyc 20180813 220023-6-5-160 ',
'P LFP 1100 CT Air2 1C CCCV 2.0cyc cold temp, 200cy 20180731 220018-4-2-162 ',
'P LFP 1100 CT Air1 1C CCCV 2.0cyc cold temp, 200cy 20180731 220018-4-1-162 ',
'P LCO 1500 CT Water1 1C CCCV 2.0cyc Coldtemp, 200cyc 20180731 220018-7-5-162 ',
'P LCO 1500 CT Air1 1C CCCV 2.0cyc Coldtemp, 200cyc 20180731 220018-7-1-162 ',
'P LCO 1500 CT Oil1 1C CCCV 2.0cyc Coldtemp, 200cyc 20180731 220018-7-3-162 ',
'P LFP 1100 CT Oil2 1C CCCV 2.0cyc cold temp, 200cy 20180731 220018-4-4-162 ',
'P LFP 1100 CT Water2 1C CCCV 2.0cyc cold temp, 200cy 20180731 220018-4-6-162 ',
'P LCO 1500 CT Water2 1C CCCV 2.0cyc Coldtemp, 200cyc 20180731 220018-7-6-162 ',
'P LFP 1100 CT Water1 1C CCCV 2.0cyc cold temp, 200cy 20180731 220018-4-5-162 ',
'P LCO 1500 CT Air2 1C CCCV 2.0cyc Coldtemp, 200cyc 20180731 220018-7-2-162 ',
'P LFP 1100 CT Oil1 1C CCCV 2.0cyc cold temp, 200cy 20180731 220018-4-3-162 ',
'P LCO 1500 CT Oil2 1C CCCV 2.0cyc Coldtemp, 200cyc 20180731 220018-7-4-162 ',
'P LCO 1500 RT Water2RR 1C CCCV 1.0cyc roomtemp, 200cyc 20180706 220018-4-7-152 ',
'P LCO 1500 WT Water1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 220023-3-4-150 ',
'C ICR 2600 WT Oil1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-5-220 ',
'C ICR 2600 WT Air2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-2-220 ',
'C ICR 2600 WT Air1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-1-220 ',
'C ICR 2600 WT Oil2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-6-220 ',
'C ICR 2600 WT Water2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-4-220 ',
'P LFP 1100 WT Air2 1C CCCV 2.0cyc warmtemp, 200cy 20180626 220023-4-2-150 ',
'P LFP 1100 WT Water1 1C CCCV 2.0cyc warmtemp, 200cy 20180626 220023-4-4-150 ',
'P LFP 1100 WT Oil2 1C CCCV 2.0cyc warmtemp, 200cy 20180626 220023-4-1-150 ',
'P LFP 1100 WT Air2 1C CCCV 2.0cyc warmtemp, 200cy 20180626 220023-4-5-150 ',
'P LFP 1100 WT Air1 1C CCCV 2.0cyc warmtemp, 200cy 20180626 220023-4-6-150 ',
'P LFP 1100 WT Water2 1C CCCV 2.0cyc warmtemp, 200cy 20180626 220023-4-3-150 ',
'C LFP 1500 WT Oil2 1C CCCV 2.0cyc warmtemp, 200cyc 20180627 230157-3-6-218 ',
'C LFP 1500 WT Oil1 1C CCCV 2.0cyc warmtemp, 200cyc 20180627 230157-3-5-219 ',
'C LFP 1500 WT Water2 1C CCCV 2.0cyc warmtemp, 200cyc 20180627 230157-3-4-219 ',
'C LFP 1500 WT Air1 1C CCCV 2.0cyc warmtemp, 200cyc 20180627 230157-3-1-219 ',
'P LCO 1500 WT Oil1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 220023-3-2-150 ',
'P LCO 1500 WT Air1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 220023-3-6-150 ',
'C LFP 1500 WT Air2 1C CCCV 2.0cyc warmtemp, 200cyc 20180627 230157-3-2-219 ',
'P LCO 1500 WT Air2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 220023-3-5-150 ',
'P LCO 1500 WT Oil2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 220023-3-1-150 ',
'C LFP 1500 WT Water1 1C CCCV 2.0cyc warmtemp, 200cyc 20180627 230157-3-3-219 ',
'C ICR 2600 WT Water1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-3-220 ',
'P LCO 1500 WT Water2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 220023-3-3-150 ',
'C ICR 2600 RT Air2 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-6-2-145 ',
'P LCO 1500 WT Water1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-3-219 ',
'P LCO 1500 WT Air2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-2-219 ',
'P LCO 1500 WT Oil2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-6-219 ',
'P LCO 1500 WT Water2 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-4-219 ',
'P LCO 1500 WT Oil1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-5-219 ',
'P LCO 1500 WT Air1 1C CCCV 2.0cyc warmtemp, 200cyc 20180626 230157-1-1-219 ',
'C ICR 2600 RT Air1 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-6-1-145 ',
'C ICR 2600 RT Oil1 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-6-3-145 ',
'C ICR 2600 RT Oil2 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-6-4-145 ',
'C ICR 2600 RT Water1 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-6-5-145 ',
'C ICR 2600 RT Water2 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-6-6-145 ',
'C LFP 1500 RT Air1 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-5-1-146 ',
'C LFP 1500 RT Water1 1C CCCV 2.0cyc roomtemp 200cyc AFTERSHORTED 20180604 220023-5-3-147 ',
'C LFP 1500 RT Air2 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-5-2-146 ',
'C LFP 1500 RT Oil2 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-5-6-146 ',
'C LFP 1500 RT Oil1 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-5-5-146 ',
'C LFP 1500 RT Water2 1C CCCV 2.0cyc roomtemp 200cyc 20180603 220023-5-4-146 ',
'P LFP 1100 RT Oil2 1C CCCV 2.0cyc roomtemp, 200cy 20180527 220023-7-6-144 ',
'P LFP 1100 RT Air2 1C CCCV 2.0cyc roomtemp, 200cy 20180527 220023-7-2-144 ',
'P LFP 1100 RT Air1 1C CCCV 2.0cyc roomtemp, 200cy 20180527 220023-7-1-144 ',
'P LCO 1500 RT Air1 1C CCCV 0.0cyc roomtemp, 200cyc 20180527 220018-7-1-145 ',
'P LCO 1500 RT Oil1 1C CCCV 0.0cyc roomtemp, 200cyc 20180527 220018-7-5-145 ',
'P LFP 1100 RT Oil1 1C CCCV 2.0cyc roomtemp, 200cy 20180527 220023-7-5-144 ',
'P LFP 1100 RT Water2 1C CCCV 2.0cyc roomtemp, 200cy 20180527 220023-7-4-144 ',
'P LFP 1100 RT Water1 1C CCCV 2.0cyc roomtemp, 200cy 20180527 220023-7-3-144 ',
'P LCO 1500 RT Air2 1C CCCV 0.0cyc roomtemp, 200cyc 20180527 220018-7-2-145 ',
'P LCO 1500 RT Oil2 1C CCCV 0.0cyc roomtemp, 200cyc 20180527 220018-7-6-145 ',
'P LCO 1500 RT Water1 1C CCCV 0.0cyc roomtemp, 200cyc 20180527 220018-7-3-145 ',
'P LCO 1500 RT Water2 1C CCCV 0.0cyc roomtemp, 200cyc 20180527 220018-7-4-145 ',
'P LCO 1500 RT Water2RR GITT-D 201.0cyc roomtemp, 200cyc 20180807 220018-4-7-159 ',
]



for s in strings:
    if 'Air' in s: print s
    
    

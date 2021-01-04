[38;5;246;03m#  reverse - Best way to create a "reversed" list in Python?[39;00m

[38;5;252mnewlist[39m[38;5;252m [39m[38;5;252m=[39m[38;5;252m [39m[38;5;252moldlist[39m[38;5;252m[[39m[38;5;252m:[39m[38;5;252m:[39m[38;5;252m-[39m[38;5;67m1[39m[38;5;252m][39m

[38;5;246;03m#  The [::-1] slicing (which my wife Anna likes to call "the Martian[39;00m
[38;5;246;03m#  smiley";-) means: slice the whole sequence, with a step of -1, i.e.,[39;00m
[38;5;246;03m#  in reverse.  It works for all sequences.[39;00m
[38;5;246;03m#  [39;00m
[38;5;246;03m#  Note that this (and the alternatives you mentioned) is equivalent to a[39;00m
[38;5;246;03m#  "shallow copy", i.e.: if the items are mutable and you call mutators[39;00m
[38;5;246;03m#  on them, the mutations in the items held in the original list are also[39;00m
[38;5;246;03m#  in the items in the reversed list, and vice versa.  If you need to[39;00m
[38;5;246;03m#  avoid that, a copy.deepcopy (while always a potentially costly[39;00m
[38;5;246;03m#  operation), followed in this case by a .reverse, is the only good[39;00m
[38;5;246;03m#  option.[39;00m

> USAGE
```
python convert_gff_id.py [prefix] [path to gff3/gff/gtf file] > [output]
```
  
> EXAMPLE
```
python convert_gff_id.py TO /work2/yuka97524/Temma/26EVM/EVM.all.gff3 > /work2/yuka97524/Temma/26EVM/EVM.all.edit.gff3
```

`EVM.all.edit.gff3`  
```
scaffold_118    EVM     gene    90592   92058   .       -       .       ID=TO.0;Name=TO.0
scaffold_118    EVM     mRNA    90592   92058   .       -       .       ID=TO.0;Parent=TO.0;Name=TO.0
scaffold_118    EVM     exon    90592   92058   .       -       .       ID=TO.0;Parent=TO.0
scaffold_118    EVM     CDS     90592   92058   .       -       0       ID=TO.0;Parent=TO.0

scaffold_118    EVM     gene    193763  193938  .       -       .       ID=TO.1;Name=TO.1
scaffold_118    EVM     mRNA    193763  193938  .       -       .       ID=TO.1;Parent=TO.1;Name=TO.1
scaffold_118    EVM     exon    193763  193938  .       -       .       ID=TO.1;Parent=TO.1
scaffold_118    EVM     CDS     193763  193938  .       -       0       ID=TO.1;Parent=TO.1
...
```

import random
from pysam import VariantFile

random.seed(snakemake.params.seed)


with VariantFile(snakemake.input[0], "r") as vcf_in:
    records = list(vcf_in)
    random.shuffle(records)

    for fraction, vcf_out in zip(snakemake.params.fractions, snakemake.output):
        with VariantFile(vcf_out, "wb", header=vcf_in.header) as vcf_out:
            for record in records[:round(len(records) * fraction)]:
                vcf_out.write(record)

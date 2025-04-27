#!  /bin/zsh
set -ex

# test form generation

for i in \
    NIPA \
    NIUnderlyingDetail \
    MNE \
    FixedAssets \
    ITA \
    IIP \
    InputOutput \
    IntlServTrade \
    IntlServSTA \
    GDPbyIndustry \
    Regional \
    UnderlyingGDPbyIndustry 
do
    QUERY_STRING="dataset=$i" python bea.py > ${i}.html
    # read nada
done

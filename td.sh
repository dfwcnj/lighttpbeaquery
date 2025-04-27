#!  /bin/zsh
set -ex

# test data retrieval

for i in \
    'DatasetName=NonSensible&TableName=None' \
    'DatasetName=NIPA&TableName=T20100&Frequency=A&Year=X&ShowMillions=No&format=HTML' \
    'DatasetName=NIPA&TableName=T20100&Frequency=A&Year=X&ShowMillions=No&format=CSV' \
    'DatasetName=NIUnderlyingDetail&TableName=U20406&Frequency=A&Year=X&format=HTML' \
    'DatasetName=NIUnderlyingDetail&TableName=U20406&Frequency=A&Year=X&format=CSV' \
    'DatasetName=MNE&DirectionOfInvestment=outward&SeriesID=all&Classification=Country&Country=308&Industry=5221&Year=all&format=HTML' \
    'DatasetName=MNE&DirectionOfInvestment=outward&SeriesID=all&Classification=Country&Country=308&Industry=5221&Year=all&format=CSV' \
    'DatasetName=FixedAssets&TableName=FAAt101&Year=X&format=HTML' \
    'DatasetName=FixedAssets&TableName=FAAt101&Year=X&format=CSV' \
    'DatasetName=ITA&Indicator=BalCurrAcct&AreaOrCountry=ALL&Frequency=A&Year=ALL&format=HTML' \
    'DatasetName=ITA&Indicator=BalCurrAcct&AreaOrCountry=ALL&Frequency=A&Year=ALL&format=CSV' \
    'DatasetName=IIP&TypeOfInvestment=CurrAndDepAssets&Component=ALL&Frequency=A&Year=ALL&format=HTML' \
    'DatasetName=IIP&TypeOfInvestment=CurrAndDepAssets&Component=ALL&Frequency=A&Year=ALL&format=CSV' \
    'DatasetName=InputOutput&TableID=57&Year=ALL&format=HTML' \
    'DatasetName=InputOutput&TableID=57&Year=ALL&format=CSV' \
    'DatasetName=IntlServTrade&TypeOfService=Engineering&TradeDirection=ALL&Affiliation=ALL&AreaOrCountry=ALL&Year=ALL&format=HTML' \
    'DatasetName=IntlServTrade&TypeOfService=Engineering&TradeDirection=ALL&Affiliation=ALL&AreaOrCountry=ALL&Year=ALL&format=CSV' \
    'DatasetName=IntlServSTA&Channel=Trade&Industry=AllInd&Destination=ALL&Affiliation=ALL&AreaOrCountry=ALL&Year=ALL&format=HTML' \
    'DatasetName=IntlServSTA&Channel=Trade&Industry=AllInd&Destination=ALL&Affiliation=ALL&AreaOrCountry=ALL&Year=ALL&format=CSV' \
    'DatasetName=GDPbyIndustry&TableID=1&Industry=ALL&Frequency=A&Year=ALL&format=HTML' \
    'DatasetName=GDPbyIndustry&TableID=1&Industry=ALL&Frequency=A&Year=ALL&format=CSV' \
    'DatasetName=Regional&TableName=CAINC4&GeoFips=COUNTY&LineCode=30&Frequency=A&Year=ALL&format=HTML' \
    'DatasetName=Regional&TableName=CAINC4&GeoFips=COUNTY&LineCode=30&Frequency=A&Year=ALL&format=CSV' \
    'DatasetName=UnderlyingGDPbyIndustry&TableID=210&Industry=ALL&Frequency=A&Year=ALL&format=HTML' \
    'DatasetName=UnderlyingGDPbyIndustry&TableID=210&Industry=ALL&Frequency=A&Year=ALL&format=CSV'
do
    QUERY_STRING="$i" python -mpdb bea.py
done

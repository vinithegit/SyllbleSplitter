import re,sys
sylObj= re.compile('(([క-హ]్)?([క-హ]్)?[క-హ]్)?[క-హ][ా-ౌ]?[\u0c00-\u0c03]?|[\u0c05-\u0c14][\u0c00-\u0c03]?')
syl=''
prevSyl=''
infile= sys.argv[1]
outfile= sys.argv[2]
with open(infile, 'r') as ifile, open(outfile,'w') as ofile:
	for line in ifile:
		buff=""
		line=line.strip().replace('\u200c',"")
		for i in line:
			prevSyl=syl
			syl=syl+i
			if(sylObj.search(syl)==None):
				continue
			if(sylObj.search(syl).group()!=syl and i!='\u0c4d' and i!='\u200d'):
				#print(prevSyl+"\t"+syl+"\t"+str(ord(i)))
				buff+=prevSyl+" "
				syl=i
		ofile.write(buff.lstrip()+syl+"\n")
		syl=''
		prevSyl=''

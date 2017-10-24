import re,sys
sylObj= re.compile('(([क-ह]़?्)?([क-ह]़?्)?[क-ह]़?्)?[क-ह]़?[ा-ौ]?[ँ-ः]?|[अ-औ][ँ-ः]?')
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
			if(sylObj.search(syl).group()!=syl and i!='्' and i!='\u200d'):
				#print(prevSyl+"\t"+syl+"\t"+str(ord(i)))
				buff+=prevSyl+" "
				syl=i
		ofile.write(buff.lstrip()+syl+"\n")
		syl=''
		prevSyl=''

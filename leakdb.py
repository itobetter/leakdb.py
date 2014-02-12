#!/bin/env python

import urllib
import optparse 
import re

def urlhash(hash, metodo):
	f = urllib.urlopen("http://api.leakdb.abusix.com/?t=%s " %hash)
	j = f.read()
	f.close()
	j = "".join(j)
	
	if re.findall("found=true", j):

		f = urllib.urlopen("http://api.leakdb.abusix.com/?t=%s " %hash)
		if metodo == "True":
			print f.read() 

		else:
			t = "".join([i for i in f.readlines() if re.match(metodo, i)])
			print t
		f.close()
	else:
		print "lo sentimos no pudimos dar con su hash"
					
if __name__=="__main__":

	parser = optparse.OptionParser("usage: %prog [options] hash")
	parser.add_option("-H", "--hash", dest="hash", default="False", type="string", help="especifique el hash/palabra que desea cifrar")
	parser.add_option("-C", "--cifrado", dest="cifrado", default="True", type="string", help="metodo de cifrado: sha1, gost, md4, md5, mysql4_mysql5, ntlm, ripemd160, sha1, sha224, sha256, sha384, sha512, whirlpool")

	(options, args) = parser.parse_args()

	if options.hash == "False":
		parser.error("pulse -h para mostrar menu de ayuda")	
	
	urlhash(options.hash, options.cifrado)

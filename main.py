from lib import *

def main():
	text='''
	十年春，齐师伐我。公将战，曹刿请见。其乡人曰：“肉食者谋之，又何间焉？”刿曰：“肉食者鄙，未能远谋。”乃入见。问：“何以战？”公曰：“衣食所安，弗敢专也，必以分人。”对曰：“小惠未遍，民弗从也。”公曰：“牺牲玉帛，弗敢加也，必以信。”对曰：“小信未孚，神弗福也。”公曰：“小大之狱，虽不能察，必以情。”对曰：“忠之属也。可以一战。战则请从。”
公与之乘，战于长勺。公将鼓之。刿曰：“未可。”齐人三鼓。刿曰：“可矣。”齐师败绩。公将驰之。刿曰：“未可。”下视其辙，登轼而望之，曰：“可矣。”遂逐齐师。
既克，公问其故。对曰：“夫战，勇气也。一鼓作气，再而衰，三而竭。彼竭我盈，故克之。夫大国，难测也，惧有伏焉。吾视其辙乱，望其旗靡，故逐之。”
'''
	print("正在生草文章...")
	grass=makeGrass(text=text,times=1)
	print("done\n正在获取音频...",end="")
	getAudio(grass)
	f=open(('out'+'.txt'),"w+",encoding="utf-8")
	f.write(grass)
	f.close()
	print("done")

if __name__ == '__main__':
	main()
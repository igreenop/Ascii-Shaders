This is my second attempt at making an img-to-ASCII converter.\nUsing the method layed out by Acerola:
img -> sobel -> invert -> get_edge_direction -> smooth_edges -> ascii (i think)

All of the filters will work by:
python3 filter.py [-d] \<file\> where file is a filename in images (not the path)

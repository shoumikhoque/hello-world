def flood_fill(image, sr, sc, color):
    if sr <0 or sc<0 or sr>=len(image) or sc>=len(image[0]) or image[sr][sc]==color:
        return image
    current_color=image[sr][sc]
    flood_fill(image,sr-1,sc,current_color)
    flood_fill(image,sr+1,sc,current_color)
    flood_fill(image,sr,sc-1,current_color)
    flood_fill(image,sr,sc+1,current_color)
    image[sr][sc]=color
    return image

if __name__ == '__main__':
    image=[[1,1,1],[1,1,0],[1,0,1]]
    sr=1
    sc=1
    color=2
    print(flood_fill(image,sr,sc,color))
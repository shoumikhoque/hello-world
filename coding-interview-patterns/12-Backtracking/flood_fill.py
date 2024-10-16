def flood_fill(image, sr, sc, target_color):
    if image[sr][sc]==target_color:
        return image
    rows,cols,=len(image),len(image[0])
    current_color=image[sr][sc]
    image[sr][sc]=target_color
    if sr-1>=0 and image[sr-1][sc]==current_color:
        image=flood_fill(image,sr-1,sc,target_color)

    if sr+1<rows and image[sr+1][sc]==current_color:
        image=flood_fill(image,sr+1,sc,target_color)

    if sc-1>=0 and image[sr][sc-1]==current_color:
        image=flood_fill(image,sr-1,sc,target_color)

    if sc+1<cols and image[sr-1][sc]==current_color:
        image=flood_fill(image,sr-1,sc,target_color)

    return image

if __name__ == '__main__':
    image=[[1,1,1],[1,1,0],[1,0,1]]
    sr=1
    sc=1
    color=2
    print(flood_fill(image,sr,sc,color))
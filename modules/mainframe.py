import customtkinter
#
main_frame = customtkinter.CTk(fg_color= '#FFBF00')
#
WIDTH = 800
HEIGHT = 600
# 
width_screen = main_frame.winfo_screenwidth() # 
height_screen = main_frame.winfo_screenheight() # 
#
x = 0 # (width_screen // 2) - (WIDTH // 2)
y = height_screen - HEIGHT #(height_screen // 2) - (HEIGHT // 2)
#
main_frame.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
#
main_frame.resizable(width= False, height= False)
#
main_frame.title('MAINFRAME')



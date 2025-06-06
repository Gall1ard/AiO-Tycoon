import objects as pr

#Standart set

items = {
    "monitors": [
        pr.Monitor("Asui S-20025", #Model is company + type + quality*100 + year
                   pr.Quality.BAD,
                   10000,
                   "1600x900",
                   "15.6''"),
        pr.Monitor("Asui S-10023",
                   pr.Quality.WORST,
                   900,
                   "1280x900",
                   "14''"),
        pr.Monitor("Asui S-10023",
                   pr.Quality.WORST,
                   900,
                   "1280x900",
                   "14''")
    ],
    "webcameras": [
        pr.WebCamera("Asui C-20024",
                     pr.Quality.BAD,
                     4000,
                     "640x320",
                     True)
    ],
    "keyboards": [
        pr.Keyboard("Asui KB-10024",
                    pr.Quality.WORST,
                    500,
                    "Medium"),
        pr.Keyboard("Asui KB-30025",
                    pr.Quality.MID,
                    3000,
                    "Medium")
    ],
    "mice": [
        pr.Mouse("Asui M-20025",
                 pr.Quality.BAD,
                 1200,
                 4000)
    ],
    "mousepads": [
        pr.MousePad("Asui MP-20023",
                    pr.Quality.BAD,
                    400,
                    "Soft")
    ]
}
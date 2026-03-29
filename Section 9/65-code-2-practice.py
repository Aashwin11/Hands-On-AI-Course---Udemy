class CameraBase:
    def __init__(self,cameraPixel):
        self.cameraPixel=cameraPixel
    
    def camera_Pixel(self):
        return self.cameraPixel

class Phone():
    camera_px=CameraBase

    def __init__(self,phone_name):
        self.camera_px=CameraBase(150)
        self.phone_name=phone_name

    def phoneName(self):
        return self.phone_name
    
samsung=Phone("Samsung")
print(f"Value: {samsung.phoneName()}")

print(f"Value from base: {samsung.camera_px.camera_Pixel()}")


        
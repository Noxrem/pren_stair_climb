# Sequenzdiagramm ObjectDetector

Sequenzdiagramm der Objekterkennung

![Sequenzdiagramm der Objekterkennung](seqObjectDetecotor.png)

```plantuml
Robot -> ObjectDetector ++: find_pictogram_start_platform
ObjectDetector -> ObjectDetector ++: _do_haar_cascade
    loop not is_found and time.time() < (start + timeout)
    ObjectDetector -> Camera ++: video_capture.read()
    return frame
    ObjectDetector -> ObjectDetector ++ : detect()
    rnote over ObjectDetector
        + cv2.cvtColor
        + detectMultiScale
    endrnote 
    alt threshold exceed 
    ObjectDetector -> ObjectDetector : is_found = True
    end 
    return
    end
    return
ObjectDetector -> Robot: found_object
```
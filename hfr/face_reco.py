import cv2
import os
import face_recognition
import pickle
from db import conn


class FaceRecog(object):
    def __init__(self):
        self.config = conn['config']

    def build_face_database(self, person_name):
        names = self.config.find_one({'name': 'names'})
        if names is None:
            self.config.insert_one(dict(name='names', value=[person_name]))
        else:
            self.config.update_one({'name': 'names'}, {'$push': {'value': person_name}})
        if not os.path.exists(person_name):
            os.mkdir(person_name)
        cap = cv2.VideoCapture(0)
        while 1:
            ret, frame = cap.read()
            cv2.imshow("cam", frame)
            if cv2.waitKey(1) & 0xFF == ord('r'):
                cv2.imwrite(person_name + "/" + person_name + ".jpeg", frame)
                # with open('name_lists.txt', 'r') as fread:
                #     name_list = pickle.load(fread)
                # name_list = []
                # name_list.append(person_name)
                # with open('name_lists.txt', 'w') as fwrite:
                #     pickle.dump(name_list, fwrite)
                break
        cap.release()
        cv2.destroyAllWindows()

    def face_recognition(self):

        # Get a reference to webcam #0 (the default one)
        video_capture = cv2.VideoCapture(0)

        # Load a sample picture and learn how to recognize it.
        image_list = []
        encoding_list = []
        # with open('name_lists.txt', 'r') as fread:
        #     name_list = pickle.load(fread)
        names = self.config.find_one({'name': 'names'})
        name_list = names['value']
        for index in range(len(name_list)):
            name = os.path.join(os.path.dirname(__file__), name_list[index] + "/" + name_list[index] + ".jpeg")
            image_list.append(face_recognition.load_image_file(name))
            encoding_list.append(face_recognition.face_encodings(image_list[index])[0])

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(small_frame)
                face_encodings = face_recognition.face_encodings(small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    match = face_recognition.compare_faces(encoding_list, face_encoding, tolerance=0.5)
                    name = "Unknown"
                    # print match
                    for index in range(len(name_list)):
                        if match[index]:
                            name = name_list[index]

                    return name
                    face_names.append(name)

            process_this_frame = not process_this_frame

            # Display the results
            # for (top, right, bottom, left), name in zip(face_locations, face_names):
            #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            #     top *= 4
            #     right *= 4
            #     bottom *= 4
            #     left *= 4
            #
            #     # Draw a box around the face
            #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            #
            #     # Draw a label with a name below the face
            #     cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            #     font = cv2.FONT_HERSHEY_DUPLEX
            #     cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            # cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    pass

    # add person
    # person_name = "fang"
    # FaceRecog().build_face_database(person_name)

    # recognition one person
    # helloName = FaceRecog().face_recognition()
    # print helloName

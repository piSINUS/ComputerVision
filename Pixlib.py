from pixellib.instance import instance_segmentation


def detectionImage():
    segment_image = instance_segmentation()
    segment_image.load_model("mask_rcnn_coco.h5")

    segment_image(
        image_path ="images/1477076675172219226.jpg",
        output_image_file = "output.jpg"
    )
def main():
    detectionImage()

if __name__ == '__main__':
    main()

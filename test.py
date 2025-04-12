from PIL import Image, ImageDraw, ImageFont
import streamlit as st

# Upload UI
st.title("Community Poster Generator")
logo_file = st.file_uploader("Upload Community Logo", type=["png", "jpg", "jpeg"])
community_name = st.text_input("Enter Community Name")

template_path = "template_social.png"

def get_font(size):
    try:
        return ImageFont.truetype("Agrandir-Wide-Bold.ttf", size)
    except:
        # fallback to Arial Bold in case font not found
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", size)

if logo_file and community_name:
    template = Image.open(template_path).convert("RGBA")
    logo = Image.open(logo_file).convert("RGBA")

    # Resize logo to height = 352px
    target_height = 800
    aspect_ratio = logo.width / logo.height
    new_logo = logo.resize((int(target_height * aspect_ratio), target_height), Image.LANCZOS)

    # Paste logo at exact position
    logo_x = (template.width - new_logo.width) // 2
    logo_y = 970

 # Draw stroke border
    draw = ImageDraw.Draw(template)
    border_thickness = 10
    border_color = "#ffbb00"
    border_box = [
        logo_x - border_thickness,
        logo_y - border_thickness,
        logo_x + new_logo.width + border_thickness,
        logo_y + new_logo.height + border_thickness
    ]
    draw.rectangle(border_box, outline=border_color, width=border_thickness)

    template.paste(new_logo, (logo_x, logo_y), new_logo)

    # Add community name
    draw = ImageDraw.Draw(template)
    font = get_font(120)
    bbox = draw.textbbox((0, 0), community_name, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (template.width - text_width) // 2
    text_y = logo_y + new_logo.height + 70
    draw.text((text_x, text_y), community_name, font=font, fill="#FFC700")

    # Show and download
    st.image(template, caption="Final Poster", use_column_width=True)
    template.save("final_poster.png")
    with open("final_poster.png", "rb") as f:
        st.download_button("Download Poster", f, file_name="poster.png")

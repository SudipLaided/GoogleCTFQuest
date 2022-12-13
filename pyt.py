set_mask_str = "gpio_set_mask"
clr_mask_str = "gpio_clr_mask"

set_masks = []
clr_masks = []

with open("chal.c", "r") as file:
    for line in file:
        set_mask_loc = line.find(set_mask_str)
        clr_mask_loc = line.find(clr_mask_str)

        end = line.find(")")

        if set_mask_loc != -1:
            set_masks.append(
                int(line[set_mask_loc + len(set_mask_str) + 1:end]))

        if clr_mask_loc != -1:
            clr_masks.append(
                int(line[clr_mask_loc + len(clr_mask_str) + 1:end]))
print(set_masks,clr_masks)
current_output = 0
flag = ""

for set_mask, clr_mask in zip(set_masks, clr_masks):
    current_output |= set_mask
    print(clr_mask,~clr_mask)
    current_output &= ~ clr_mask
    flag += chr(current_output)

print(flag.strip())


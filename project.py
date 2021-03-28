
f = scipy.misc.face(gray=True)
f = f[230:290, 220:320]

noisy = cv2.imread('rose.png')



gauss_denoised = ndimage.gaussian_filter(noisy, 2)
med_denoised = ndimage.median_filter(noisy, 3)


plt.figure(figsize=(8,10))


ax=plt.subplot(131)
plt.imshow(noisy, cmap=plt.cm.gray, vmin=400, vmax=820)
plt.axis('off')
plt.title('noisy', fontsize=20)
plt.subplot(133)
plt.imshow(gauss_denoised, cmap=plt.cm.gray, vmin=400, vmax=820)
plt.axis('off')
plt.title('Denoised', fontsize=20)


plt.subplots_adjust(wspace=0, hspace=0, top=0.9, bottom=0, left=0,
                    right=1)
plt.show()

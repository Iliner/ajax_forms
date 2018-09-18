from django.db import models

# Create your models here.




class Goods(models.Model):
	code = models.CharField(max_length=30, unique=True)
	articul = models.CharField(max_length=30)
	producer = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	in_stock = models.CharField(max_length=20, null=True, blank=True)
	price = models.FloatField()	
	photo = models.ForeignKey('Photo', blank=True, null=True)
	order_count = models.PositiveSmallIntegerField(blank=True, null=True)
	
	def get_in_stock(self):
		if in_stock:
			return '+'
		else:
			return ''


	def __str__(self):
		return "{}".format(self.code)

	class Meta:
		unique_together = ('code', 'articul')
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'
		ordering = ['code']



class Photo(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(null=True)
	date = models.DateTimeField(auto_now=True)	
	photo_width = models.IntegerField(default=0)
	photo_height = models.IntegerField(default=0)
	photo = models.ImageField()
	code = models.IntegerField()

	image_url = models.URLField(null=True, blank=True)


	def get_remote_image(self):
		if self.image_url and not self.photo:
			result = urllib.urlretrieve(self.image_url)
			self.photo.save(os.path.basename(self.name + self.image_url.rsplit('.')[-1]), File(open(result[0])))
			self.save()




	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('index:detail', kwargs={'id': self.id})

	def change_size_img(self):
		#Opening the uploaded image
		im = Image.open(self.photo)

		output = BytesIO()

		#Resize/modify the image
		im = im.resize((self.photo_width, self.photo_height))

		#after modifications, save it to the output
		im.save(output, format='PNG', quality=100)
		output.seek(0)

		#change the imagefield value to be the newley modifed image value
		self.photo = InMemoryUploadedFile(output,'ImageField', "%s.png" %self.photo.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)


	class Meta:
		ordering = ['date']
		verbose_name = 'Изображение'
		verbose_name_plural = 'Изображения'
from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from minerals.models import Mineral


class MineralModelTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
          name="Rock",
          image_filename="imagefile",
          image_caption="imagetitle",
          category="a category",
          formula="some fomular",
          strunz_classification="whats classified",
          crystal_system="oooooh",
          unit_cell="lots of them",
          color="dirty",
          crystal_symmetry="not",
          cleavage="notewothy",
          mohs_scale_hardness="rock hard",
          luster="smooth",
          streak="when broken",
          diaphaneity="???",
          optical_properties="looks like a rock",
          refractive_index="nope",
          crystal_habit="under pressure",
          specific_gravity="does not float",
          group="dirt")

    def test_mineral_creation(self):
        rock = Mineral.objects.get(name="Rock")
        self.assertTrue(isinstance(self.mineral, Mineral))
        self.assertEqual(str(self.mineral), rock.name)


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
          name="Rock",
          image_filename="imagefile",
          image_caption="imagetitle",
          category="a category",
          formula="some fomular",
          strunz_classification="whats classified",
          crystal_system="oooooh",
          unit_cell="lots of them",
          color="dirty",
          crystal_symmetry="not",
          cleavage="notewothy",
          mohs_scale_hardness="rock hard",
          luster="smooth",
          streak="when broken",
          diaphaneity="???",
          optical_properties="looks like a rock",
          refractive_index="nope",
          crystal_habit="under pressure",
          specific_gravity="does not float",
          group="dirt")

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    def test_mineral_random_view(self):
        resp = self.client.get(reverse('minerals:random'))
        resp2 = self.client.get(reverse('minerals:random'))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertNotEqual(resp, resp2)

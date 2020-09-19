from libdecsync import Decsync
import unittest
import shutil

# Very basic tests, mostly to make sure no crashes occur
class DecsyncTest(unittest.TestCase):

    def test_instance(self):
        decsync = Decsync(".tests/decsync", "sync-type", None, "app-id")
        extra = {}
        def listener(path, datetime, key, value, extra):
            extra[(tuple(path), key)] = value
        decsync.add_listener([], listener)

        decsync.set_entry(["foo1", "bar1"], "key1", "value1 ☺")
        decsync.set_entries([Decsync.EntryWithPath(["foo2", "bar2"], "key2", "value2")])
        decsync.set_entries_for_path(["foo3", "bar3"], [Decsync.Entry("key3", "value3")])

        decsync.execute_all_new_entries(extra)

        decsync.execute_stored_entry(["foo1", "bar1"], "key1", extra)
        decsync.execute_stored_entries([Decsync.StoredEntry(["foo2", "bar2"], "key2")], extra)
        decsync.execute_stored_entries_for_path_exact(["foo3", "bar3"], extra, keys=["key3"])

        self.assertEqual(extra[(("foo1", "bar1"), "key1")], "value1 ☺")
        self.assertEqual(extra[(("foo2", "bar2"), "key2")], "value2")
        self.assertEqual(extra[(("foo3", "bar3"), "key3")], "value3")

        extra = {}

        decsync.execute_stored_entries_for_path_exact(["foo1", "bar1"], extra)
        decsync.execute_stored_entries_for_path_prefix(["foo2"], extra, keys=["key2"])
        decsync.execute_stored_entries_for_path_prefix(["foo3"], extra)

        self.assertEqual(extra[(("foo1", "bar1"), "key1")], "value1 ☺")
        self.assertEqual(extra[(("foo2", "bar2"), "key2")], "value2")
        self.assertEqual(extra[(("foo3", "bar3"), "key3")], "value3")

        decsync.init_stored_entries()
        self.assertEqual(decsync.latest_app_id(), "app-id")

    def test_static(self):
        Decsync(".tests/decsync", "sync-type", "collection", "app-id").set_entry(["info"], "name", "Foo")
        self.assertEqual(Decsync.get_static_info(".tests/decsync", "sync-type", "collection", "name"), "Foo")
        self.assertEqual(Decsync.get_static_info(".tests/decsync", "sync-type", "collection", "color"), None)
        self.assertEqual(Decsync.list_collections(".tests/decsync", "sync-type"), ["collection"])
        Decsync.get_app_id("app", id=12345)
        Decsync.get_app_id("app")

    def tearDown(self):
        shutil.rmtree(".tests", ignore_errors=True)

if __name__ == '__main__':
    unittest.main()

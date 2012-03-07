from spec import Spec, skip, eq_

from invoke.collection import Collection


def _mytask():
    print "woo!"


class Collection_(Spec):
    class add_task:
        def associates_given_callable_with_given_name(self):
            c = Collection()
            c.add_task('foo', _mytask)
            eq_(c.get('foo'), _mytask)

        def allows_specifying_aliases(self):
            skip()

        def allows_flagging_as_default(self):
            skip()

        def raises_ValueError_on_multiple_defaults(self):
            skip()

    class add_collection:
        def adds_collection_as_subcollection_of_self(self):
            skip()

    class get:
        def finds_own_tasks_by_name(self):
            # TODO: duplicates an add_task test above, fix?
            c = Collection()
            c.add_task('foo', _mytask)
            eq_(c.get('foo'), _mytask)

        def finds_subcollection_tasks_by_dotted_name(self):
            skip()

        def honors_aliases_in_own_tasks(self):
            skip()

        def honors_subcollection_aliases(self):
            skip()

        def honors_own_default_task_on_empty_string(self):
            skip()

        def honors_subcollection_default_tasks_on_subcollection_name(self):
            skip()

        def is_aliased_to_dunder_getitem(self):
            "is aliased to __getitem__"
            skip()
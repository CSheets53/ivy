# global
from typing import Dict, List, Optional, Union

# local
import ivy
from ivy.container.base import ContainerBase

# ToDo: implement all methods here as public instance methods


# noinspection PyMissingConstructor
class ContainerWithSet(ContainerBase):
    @staticmethod
    def static_unique_counts(
        x: ivy.Container,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        *,
        out: Optional[ivy.Container] = None,
    ) -> ivy.Container:
        """
        ivy.Container static method variant of ivy.unique_counts. This method simply wraps the
        function, and so the docstring for ivy.unique_counts also applies to this method
        with minimal changes.

        Examples
        --------
        With :code:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([0., 1., 3. , 2. , 1. , 0.]), b=ivy.array([1,2,1,3,4,1,3]))
        >>> y = x.static_unique_counts()
        >>> print(y)
        {
            a: Tuple([0., 1., 2., 3.],[2,2,1,1]),
            b: Tuple([1,2,3,4],[3,1,2,1])
        }
        """
        return ContainerBase.multi_map_in_static_method(
            "unique_counts",
            x,
            key_chains=key_chains,
            to_apply=to_apply,
            prune_unapplied=prune_unapplied,
            map_sequences=map_sequences,
            out=out,
        )

    def unique_counts(
        self: ivy.Container,
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        *,
        out: Optional[ivy.Container] = None
    ) -> ivy.Container:
        """
        ivy.Container instance method variant of ivy.unique_counts. This method simply wraps the
        function, and so the docstring for ivy.unique_counts also applies to this method
        with minimal changes.

        Examples
        --------
        With :code:`ivy.Container` input:

        >>> x = ivy.Container(a=ivy.array([0., 1., 3. , 2. , 1. , 0.]), b=ivy.array([1,2,1,3,4,1,3]))
        >>> y = x.unique_counts()
        >>> print(y)
        {
            a: Tuple([0., 1., 2., 3.],[2,2,1,1]),
            b: Tuple([1,2,3,4],[3,1,2,1])
        }
        """
        return self.static_unique_counts(
            self, key_chains, to_apply, prune_unapplied, map_sequences, out=out
        )
